from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

# create an instance of the API class
api_instance = client.BatchV1Api()
namespace = 'default' # str | object name and auth scope, such as for teams and projects
body = client.V1Job(metadata=client.V1ObjectMeta(name="job1"),spec=client.V1JobSpec(template=client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(name="job1spec"),spec=client.V1PodSpec(containers=[client.V1Container(image="busybox",name="job1ctr1",command=["echo","Hello World"])],restart_policy="Never"))))
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
#body=client.V1Job()
try: 
    api_response = api_instance.create_namespaced_job(namespace, body, pretty=pretty)
except ApiException as e:
    print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
