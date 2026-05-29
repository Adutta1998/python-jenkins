pipeline {
    agent any

    environment {
        PATH = "${HOME}/.local/bin:${PATH}"
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
                    uv sync
                '''
            }
        }

        stage('Run') {
            steps {
                sh '''
                    uv run python main.py
                '''
            }
        }
    }
}