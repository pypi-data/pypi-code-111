from distutils.core import setup
setup(
  name = 'gbsoft',         # How you named your package folder (MyLib)
  packages = ['gbsoft'],   # Chose the same as "name"
  version = '0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'custom OpenCV library',   # Give a short description about your library
  author = 'Ganesh Attarde',                   # Type in your name
  author_email = 'ganesh@gbsoftronics.com',      # Type in your E-Mail
  url = 'https://github.com/arduinoganesh/gbsoft',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/arduinoganesh/gbsoft.git',    # I explain this later on
  keywords = ['ARDUINO', 'OPENCV-PYTHON', 'OPENCV-ARDUINO','FACE-DETECTOR','HAND-DETECTOR','FACEMESHDETECTOR','POSE-DETECTOR'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python',
          'mediapipe',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)