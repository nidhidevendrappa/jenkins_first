pipeline {
    agent any

    environment {
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
                echo '🐍 Checking virtual environment...'
                bat '''
                    @echo off

                    REM ✅ Step 1: Create venv ONLY if it does not already exist
                    IF NOT EXIST %VENV_DIR%\\Scripts\\activate.bat (
                        echo [INFO] venv not found. Creating virtual environment...
                        python -m venv %VENV_DIR%
                    ) ELSE (
                        echo [INFO] venv already exists. Skipping creation.
                    )

                    REM ✅ Step 2: Activate venv
                    call %VENV_DIR%\\Scripts\\activate

                    REM ✅ Step 3: Reinstall packages ONLY if requirements.txt has changed
                    REM   Compare checksum of requirements.txt with last saved checksum
                    certutil -hashfile requirements.txt MD5 > requirements_current.md5
                    IF EXIST requirements_last.md5 (
                        FC /B requirements_current.md5 requirements_last.md5 >nul 2>&1
                        IF ERRORLEVEL 1 (
                            echo [INFO] requirements.txt changed. Installing packages...
                            pip install --upgrade pip
                            pip install -r requirements.txt
                            copy /Y requirements_current.md5 requirements_last.md5
                        ) ELSE (
                            echo [INFO] requirements.txt unchanged. Skipping pip install.
                        )
                    ) ELSE (
                        echo [INFO] First run. Installing packages...
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        copy /Y requirements_current.md5 requirements_last.md5
                    )
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
