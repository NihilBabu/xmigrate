# Import the needed management objects from the libraries. The azure.common library
# is installed automatically with the other libraries.
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from model import blueprint, project
from utils import dbconn



async def create_vm_worker(rg_name, vm_name, location, username, password, vm_type, nic_id, subscription_id, image_name):
    compute_client = get_client_from_cli_profile(ComputeManagementClient)
    print(
        "Provisioning virtual machine {vm_name}; this operation might take a few minutes.")
    poller = compute_client.virtual_machines.create_or_update(rg_name, vm_name,
                                                              {
                                                                  "location": location,
                                                                  "storage_profile": {
                                                                      "image_reference": {
                                                                          'id': '/subscriptions/' + subscription_id + '/resourceGroups/' + rg_name + '/providers/Microsoft.Compute/images/'+image_name
                                                                      }
                                                                  },
                                                                  "hardware_profile": {
                                                                      "vm_size": vm_type
                                                                  },
                                                                  "os_profile": {
                                                                      "computer_name": vm_name,
                                                                      "admin_username": username,
                                                                      "admin_password": password
                                                                  },
                                                                  "network_profile": {
                                                                      "network_interfaces": [{
                                                                          "id": nic_id,
                                                                      }]
                                                                  }
                                                              }
                                                              )

    vm_result = poller.result()
    print("Provisioned virtual machine")
    try:
        BluePrint.objects(project=project, host=vm_name).update(vm_id=vm_result.name,status=100)
    except:
        print("disk creation updation failed")
    finally:
        con.close()


async def create_vm(project):
    con = dbconn()
    rg_name = Project.objects(project=project).to_json()['resource_group']
    location = Project.objects(project=project).to_json()['location']
    subscription_id = Project.objects(project=project).to_json()['subscription_id']
    username = "xmigrate"
    password = "xmigrate"
    machines = BluePrint.objects.to_json()
    for machine in machines:
        vm_name = machine['host']
        vm_type = machine['machine_type']
        nic_id = machine['nic_id']
        image_name = machine['image_id']
        await(asyncio.create_task(create_vm_worker(rg_name, vm_name, location, username, password, vm_type, nic_id, subscription_id, image_name)))
    con.close()