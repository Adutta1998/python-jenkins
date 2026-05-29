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
                    curl -LsSf https://astral.sh/uv/install.sh | sh
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