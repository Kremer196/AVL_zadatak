import subprocess

def deploy():
        service1_deploy = f'kubectl apply -f service1\service1\service1-deplyoment.yaml'
        service1_service = f'kubectl apply -f service1\service1\service1-service.yaml'

        service2_deploy = f'kubectl apply -f service2\service2\service2-deployment.yaml'
        service2_service = f'kubectl apply -f service2\service2\service2-service.yaml'

        subprocess.run(service1_deploy, shell=True, check=True)
        subprocess.run(service1_service, shell=True, check=True)

        subprocess.run(service2_deploy, shell=True, check=True)
        subprocess.run(service2_service, shell=True, check=True)

if __name__ == '__main__':
        deploy()