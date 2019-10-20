  73  git clone https://github.com/mkambie/lambda-publish-zip.git
   75  cd lambda-publish-zip/
   81  python --version
   86  python -m venv venv 						//Install a python virtual environment in /venv directory
   97  source venv/Scripts/activate 			//Activate Virtual Environment 
   99  pip install requests						//Use pip to install required depedencies
  100  touch my_handler.py						//We write our python lambda function
  103  pip freeze > requirements.txt			//We are putting all dependencies of requests inside file
  104  cat requirements.txt					 
  105  pip install -r requirements.txt -t .		//We install dependencies of main dependency (requests) on current directory
  107  deactivate 								//We deactivate virtual environment
  108  rm -r venv/								//Remove virtual env directory

  //Open our directory and zip all contents to upload in lambda console

  
  //Python Req put:
  https://www.programcreek.com/python/example/2253/requests.put