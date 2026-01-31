pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            args '--shm-size=2g'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python --version
                python -m venv venv
                . venv/bin/activate
                which python
                python -m pip install --upgrade pip --no-cache-dir
                pip install -r requirements.txt
                pytest
                '''
            }
        }

    }


}
