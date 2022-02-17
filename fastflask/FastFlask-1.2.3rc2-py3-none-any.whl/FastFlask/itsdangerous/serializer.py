import json
import typing as _t

from .encoding import want_bytes
from .exc import BadPayload
from .exc import BadSignature
from .signer import _make_keys_list
from .signer import Signer

_t_str_bytes = _t.Union[str, bytes]
_t_opt_str_bytes = _t.Optional[_t_str_bytes]
_t_kwargs = _t.Dict[str, _t.Any]
_t_opt_kwargs = _t.Optional[_t_kwargs]
_t_signer = _t.Type[Signer]
_t_fallbacks = _t.List[_t.Union[_t_kwargs, _t.Tuple[_t_signer, _t_kwargs], _t_signer]]
_t_load_unsafe = _t.Tuple[bool, _t.Any]
_t_secret_key = _t.Union[_t.Iterable[_t_str_bytes], _t_str_bytes]


def is_text_serializer(serializer: _t.Any) -> bool:
    """Checks whether a serializer generates text or binary."""
    return isinstance(serializer.dumps({}), str)


class Serializer:
    """A serializer wraps a :class:`~itsdangerous.signer.Signer` to
    enable serializing and securely signing data other than bytes. It
    can unsign to verify that the data hasn't been changed.

    The serializer provides :meth:`dumps` and :meth:`loads`, similar to
    :mod:`json`, and by default uses :mod:`json` internally to serialize
    the data to bytes.

    The secret key should be a random string of ``bytes`` and should not
    be saved to code or version control. Different salts should be used
    to distinguish signing in different contexts. See :doc:`/concepts`
    for information about the security of the secret key and salt.

    :param secret_key: The secret key to sign and verify with. Can be a
        list of keys, oldest to newest, to support key rotation.
    :param salt: Extra key to combine with ``secret_key`` to distinguish
        signatures in different contexts.
    :param serializer: An object that provides ``dumps`` and ``loads``
        methods for serializing data to a string. Defaults to
        :attr:`default_serializer`, which defaults to :mod:`json`.
    :param serializer_kwargs: Keyword arguments to pass when calling
        ``serializer.dumps``.
    :param signer: A ``Signer`` class to instantiate when signing data.
        Defaults to :attr:`default_signer`, which defaults to
        :class:`~itsdangerous.signer.Signer`.
    :param signer_kwargs: Keyword arguments to pass when instantiating
        the ``Signer`` class.
    :param fallback_signers: List of signer parameters to try when
        unsigning with the default signer fails. Each item can be a dict
        of ``signer_kwargs``, a ``Signer`` class, or a tuple of
        ``(signer, signer_kwargs)``. Defaults to
        :attr:`default_fallback_signers`.

    .. versionchanged:: 2.0
        Added support for key rotation by passing a list to
        ``secret_key``.

    .. versionchanged:: 2.0
        Removed the default SHA-512 fallback signer from
        ``default_fallback_signers``.

    .. versionchanged:: 1.1
        Added support for ``fallback_signers`` and configured a default
        SHA-512 fallback. This fallback is for users who used the yanked
        1.0.0 release which defaulted to SHA-512.

    .. versionchanged:: 0.14
        The ``signer`` and ``signer_kwargs`` parameters were added to
        the constructor.
    """

    #: The default serialization module to use to serialize data to a
    #: string internally. The default is :mod:`json`, but can be changed
    #: to any object that provides ``dumps`` and ``loads`` methods.
    default_serializer: _t.Any = json

    #: The default ``Signer`` class to instantiate when signing data.
    #: The default is :class:`itsdangerous.signer.Signer`.
    default_signer: _t_signer = Signer

    #: The default fallback signers to try when unsigning fails.
    default_fallback_signers: _t_fallbacks = []

    def __init__(
        self,
        secret_key: _t_secret_key,
        salt: _t_opt_str_bytes = b"itsdangerous",
        serializer: _t.Any = None,
        serializer_kwargs: _t_opt_kwargs = None,
        signer: _t.Optional[_t_signer] = None,
        signer_kwargs: _t_opt_kwargs = None,
        fallback_signers: _t.Optional[_t_fallbacks] = None,
    ):
        #: The list of secret keys to try for verifying signatures, from
        #: oldest to newest. The newest (last) key is used for signing.
        #:
        #: This allows a key rotation system to keep a list of allowed
        #: keys and remove expired ones.
        self.secret_keys: _t.List[bytes] = _make_keys_list(secret_key)

        if salt is not None:
            salt = want_bytes(salt)
            # if salt is None then the signer's default is used

        self.salt = salt

        if serializer is None:
            serializer = self.default_serializer

        self.serializer: _t.Any = serializer
        self.is_text_serializer: bool = is_text_serializer(serializer)

        if signer is None:
            signer = self.default_signer

        self.signer: _t_signer = signer
        self.signer_kwargs: _t_kwargs = signer_kwargs or {}

        if fallback_signers is None:
            fallback_signers = list(self.default_fallback_signers or ())

        self.fallback_signers: _t_fallbacks = fallback_signers
        self.serializer_kwargs: _t_kwargs = serializer_kwargs or {}

    @property
    def secret_key(self) -> bytes:
        """The newest (last) entry in the :attr:`secret_keys` list. This
        is for compatibility from before key rotation support was added.
        """
        return self.secret_keys[-1]

    def load_payload(
        self, payload: bytes, serializer: _t.Optional[_t.Any] = None
    ) -> _t.Any:
        """Loads the encoded object. This function raises
        :class:`.BadPayload` if the payload is not valid. The
        ``serializer`` parameter can be used to override the serializer
        stored on the class. The encoded ``payload`` should always be
        bytes.
        """
        if serializer is None:
            serializer = self.serializer
            is_text = self.is_text_serializer
        else:
            is_text = is_text_serializer(serializer)

        try:
            if is_text:
                return serializer.loads(payload.decode("utf-8"))

            return serializer.loads(payload)
        except Exception as e:
            raise BadPayload(
                "Could not load the payload because an exception"
                " occurred on unserializing the data.",
                original_error=e,
            )

    def dump_payload(self, obj: _t.Any) -> bytes:
        """Dumps the encoded object. The return value is always bytes.
        If the internal serializer returns text, the value will be
        encoded as UTF-8.
        """
        return want_bytes(self.serializer.dumps(obj, **self.serializer_kwargs))

    def make_signer(self, salt: _t_opt_str_bytes = None) -> Signer:
        """Creates a new instance of the signer to be used. The default
        implementation uses the :class:`.Signer` base class.
        """
        if salt is None:
            salt = self.salt

        return self.signer(self.secret_keys, salt=salt, **self.signer_kwargs)

    def iter_unsigners(self, salt: _t_opt_str_bytes = None) -> _t.Iterator[Signer]:
        """Iterates over all signers to be tried for unsigning. Starts
        with the configured signer, then constructs each signer
        specified in ``fallback_signers``.
        """
        if salt is None:
            salt = self.salt

        yield self.make_signer(salt)

        for fallback in self.fallback_signers:
            if isinstance(fallback, dict):
                kwargs = fallback
                fallback = self.signer
            elif isinstance(fallback, tuple):
                fallback, kwargs = fallback
            else:
                kwargs = self.signer_kwargs

            for secret_key in self.secret_keys:
                yield fallback(secret_key, salt=salt, **kwargs)

    def dumps(self, obj: _t.Any, salt: _t_opt_str_bytes = None) -> _t_str_bytes:
        """Returns a signed string serialized with the internal
        serializer. The return value can be either a byte or unicode
        string depending on the format of the internal serializer.
        """
        payload = want_bytes(self.dump_payload(obj))
        rv = self.make_signer(salt).sign(payload)

        if self.is_text_serializer:
            return rv.decode("utf-8")

        return rv

    def dump(self, obj: _t.Any, f: _t.IO, salt: _t_opt_str_bytes = None) -> None:
        """Like :meth:`dumps` but dumps into a file. The file handle has
        to be compatible with what the internal serializer expects.
        """
        f.write(self.dumps(obj, salt))

    def loads(
        self, s: _t_str_bytes, salt: _t_opt_str_bytes = None, **kwargs: _t.Any
    ) -> _t.Any:
        """Reverse of :meth:`dumps`. Raises :exc:`.BadSignature` if the
        signature validation fails.
        """
        s = want_bytes(s)
        last_exception = None

        for signer in self.iter_unsigners(salt):
            try:
                return self.load_payload(signer.unsign(s))
            except BadSignature as err:
                last_exception = err

        raise _t.cast(BadSignature, last_exception)

    def load(self, f: _t.IO, salt: _t_opt_str_bytes = None) -> _t.Any:
        """Like :meth:`loads` but loads from a file."""
        return self.loads(f.read(), salt)

    def loads_unsafe(
        self, s: _t_str_bytes, salt: _t_opt_str_bytes = None
    ) -> _t_load_unsafe:
        """Like :meth:`loads` but without verifying the signature. This
        is potentially very dangerous to use depending on how your
        serializer works. The return value is ``(signature_valid,
        payload)`` instead of just the payload. The first item will be a
        boolean that indicates if the signature is valid. This function
        never fails.

        Use it for debugging only and if you know that your serializer
        module is not exploitable (for example, do not use it with a
        pickle serializer).

        .. versionadded:: 0.15
        """
        return self._loads_unsafe_impl(s, salt)

    def _loads_unsafe_impl(
        self,
        s: _t_str_bytes,
        salt: _t_opt_str_bytes,
        load_kwargs: _t_opt_kwargs = None,
        load_payload_kwargs: _t_opt_kwargs = None,
    ) -> _t_load_unsafe:
        """Low level helper function to implement :meth:`loads_unsafe`
        in serializer subclasses.
        """
        if load_kwargs is None:
            load_kwargs = {}

        try:
            return True, self.loads(s, salt=salt, **load_kwargs)
        except BadSignature as e:
            if e.payload is None:
                return False, None

            if load_payload_kwargs is None:
                load_payload_kwargs = {}

            try:
                return (
                    False,
                    self.load_payload(e.payload, **load_payload_kwargs),
                )
            except BadPayload:
                return False, None

    def load_unsafe(self, f: _t.IO, salt: _t_opt_str_bytes = None) -> _t_load_unsafe:
        """Like :meth:`loads_unsafe` but loads from a file.

        .. versionadded:: 0.15
        """
        return self.loads_unsafe(f.read(), salt=salt)
