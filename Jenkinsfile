pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vinaykondru/pytestframework.git']])
            }
        }
        stage('Build') {
            steps {
                sh '''python3 --version
python3 -m pip install --upgrade pip
python3 -m pip install pytest
python3 -m pip install pytest selenium
python3 -m pip install webdriver-manager
python3 -m pytest tests

                    '''
            }
        }
    }
}
