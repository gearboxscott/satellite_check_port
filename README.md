# satellite_check_port
This python script will check to see if port are open to the Satellite 6 Server from the client

Steps:

. Download the check_port.py on any potential Satellite 6.x client.
. Change the permissions to 700:
.. `./check_port.py satellite_server.fqdn`
. See the output, you can Ctrl-C out of it if it stops on a port that doesn't return or wait for the timeout.
