You can try running it by:

1. Cloning the repo
2. Set up venv using Python 10

   Run 
   $env:CUDACXX="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/bin/nvcc.exe"
   $env:CMAKE_ARGS="-DGGML_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=75"
   pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade
4. Install requirements.txt


Note: You need Cuda 11.8
