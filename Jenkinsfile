pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup uv') {
            steps {
                sh '''
                    python3 -m pip install --user uv
                    export PATH=$HOME/.local/bin:$PATH

                    uv venv .venv
                    . .venv/bin/activate

                    uv sync
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    . .venv/bin/activate
                    uv run python main.py
                '''
            }
        }
    }
}