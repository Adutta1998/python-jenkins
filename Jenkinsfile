pipeline {
    agent any

    environment {
        PATH = "${env.HOME}/.local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup uv') {
            steps {
                sh '''
                    curl -LsSf https://astral.sh/uv/install.sh | sh

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