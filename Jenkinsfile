pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository from GitHub
                git branch: 'main', url: 'https://github.com/MaXIP21/Due-Date-Calculator.git'
            }
        }
        stage('Setup virtual environment') {
            steps {
                // Create a virtual environment and activate it
                sh '''#!/bin/bash
                    python3 -m venv ${BUILD_TAG} 
                    source ${BUILD_TAG}/bin/activate
                    pwd
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                // Install dependencies, assuming you're using pip
                sh '''#!/bin/bash
                    ${BUILD_TAG}/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Run tests') {
            steps {
                // Run pytest with XML output
                sh '${BUILD_TAG}/bin/pytest --junitxml=reports/calculate-due-date-test-results.xml unit_test_calculate_due_date.py'
                sh '${BUILD_TAG}/bin/pytest --junitxml=reports/datecalculator-test-results.xml unit_test_datecaclulator.py'
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'reports/*.xml'
                    junit allowEmptyResults: true, testResults: 'reports/datecalculator-test-results.xml'
                }
            }
        }
    }
    post {
        always {
            sh '''#/bin/bash
                rm -rf ${BUILD_TAG}
            '''
        }
    }
}