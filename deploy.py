import subprocess
import argparse

def deploy(version_service1, version_service2, port_service1, port_service2):
    service1_run = f'docker run -d --name service1 -p {port_service1}:8080 localhost:5000/service1:{version_service1}'
    subprocess.run(service1_run, shell=True, check=True)

    service2_run = f'docker run -d --name service2 -p {port_service2}:8080 localhost:5000/service2:{version_service2}'
    subprocess.run(service2_run, shell=True, check=True)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--version_service1', required=True)
    parser.add_argument('--version_service2', required=True)
    parser.add_argument('--port_service1', required=True)
    parser.add_argument('--port_service2', required=True)

    args = parser.parse_args()

    deploy(args.version_service1, args.version_service2, args.port_service1, args.port_service2)