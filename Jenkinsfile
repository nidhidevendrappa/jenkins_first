pipeline {
    agent any

    environment {
        // Set your Python venv path
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Pulling latest code from Git...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                // Windows
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running unit tests...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pytest tests/ -v --tb=short
                '''
            }
        }

        stage('Build') {
            steps {
                echo '🏗️ Build stage — package or compile your app here'
                echo 'Build successful!'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying application...'
                echo 'Deployment complete!'
                // Add your real deploy command here, e.g.:
                // bat 'call %VENV_DIR%\\Scripts\\activate && python app.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs above.'
        }
        always {
            echo '🔁 Pipeline finished — cleaning up if needed.'
        }
    }
}
