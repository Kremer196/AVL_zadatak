import subprocess

def deploy():
        service1_helm = f'helm install service1-release service1-chart'
        service2_helm = f'helm install service2-release service2-chart'

        subprocess.run(service1_helm, shell=True, check=True)
        subprocess.run(service2_helm, shell=True, check=True)


if __name__ == '__main__':
        deploy()