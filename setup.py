import setuptools

setuptools.setup(
    name='lisa',
    version='0.1',
    author='LISA',
    author_email='LISA@LISA.com',
    description="LISA",
    url='https://github.com/dvlab-research/LISA',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=[
        "bitsandbytes",
        "transformers",
        "Pillow",
        "numpy",
        "einops",
        "sentencepiece",
        "torch",
        "torchvision",
    ], 
    extras_require={
    },
    include_package_data=True,
)
