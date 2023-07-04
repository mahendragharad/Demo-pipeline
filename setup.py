# To make this folder as the package 
# We need to do this 
# Create the one file inside each folder as __init__

from setuptools import setup , find_packages

setup(name="Censuse-Income",
      version="0.0.1",
      author="mahendra",
      author_email="mahendragharad035@gmail.com",
      packages=find_packages(),
      install_requires = ["pandas","numpy","flask"]
    )

# Where there is __init__ file in the folder it consider it as the 
# package 