from __future__ import annotations

import abc
from typing import Optional

import attr
import zmq


@attr.dataclass(frozen=True, slots=True)
class AuthResult:
    success: bool
    user_id: Optional[str] = None


@attr.dataclass(frozen=True, slots=True)
class Identity:
    domain: str
    private_key: bytes


def create_keypair(self):
    '''
    Generate a new CURVE-25519 public-private keypair.
    '''
    # NOTE: currently we rely on zmq for convenience, but we may use libnacl directly
    #       if we want to isolate this module from zmq dependency.
    public_key, private_key = zmq.curve_keypair()
    return public_key, private_key


class AbstractAuthenticator(metaclass=abc.ABCMeta):
    '''
    Users of Callosum should subclass this to implement custom authentication.

    Though `lower.zeromq` uses the keypair to encrypt the traffic as well as
    authenticate the peer sockets, but this is not a mandatory requirement for
    transport implementations.  A transport may simply use its own network-level
    encryption and/or authentication scheme while leaving this authenticator as an
    application-level identity management scheme.
    '''

    # === Binder APIs ===

    @abc.abstractmethod
    async def server_identity(self) -> Identity:
        '''
        Return the identity of the server.
        Only used by the binder.
        '''
        raise NotImplementedError

    @abc.abstractmethod
    async def check_client(self, client_id: Identity) -> AuthResult:
        '''
        Check if the given domain and client public key is a valid one or not.
        Only used by the binder.
        '''
        raise NotImplementedError

    # === Connector APIs ===

    @abc.abstractmethod
    async def server_public_key(self) -> bytes:
        '''
        Return the public key of the server.
        Only used by the connector.
        '''
        raise NotImplementedError

    @abc.abstractmethod
    async def client_identity(self) -> Identity:
        '''
        Return the identity of the client.
        Only used by the connector.
        '''
        raise NotImplementedError

    @abc.abstractmethod
    async def client_public_key(self) -> bytes:
        '''
        Return the public key of the client.
        Only used by the connector.
        '''
        raise NotImplementedError
