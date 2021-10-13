# Message Queue

PvSimulator Message Queue
Python Interpreter 3.8.3
David Loerinci

Required installations:

1. Install pika module:
   Windows: python -m pip install pika
   Debian / Ubuntu: sudo apt-get install -y python3-pika

2. Install Erlang:
   Windows: https://www.erlang.org/downloads

3. Install RabbitMQ Server:
   Windows: https://www.rabbitmq.com/install-windows.html
   Debian / Ubuntu: sudo apt-get install rabbitmq-server

Run the workflow:

- Do not change the folder structure
- Execute the file PV_QUEUE/Queue/control_queue.py
- The RabbitMQ Queue name can be defined in the file PV_QUEUE/Queue/Input/config.json and is currently set to "pv_challenge_workflow". The queue name will be completed by a random number, so the code will create a fresh queue with every launch.
- Within the config.json file the sunset is set to 8 a.m. and the sunset is set to 8 p.m. (20). The twilight time period is set to 1.5 hours and the maximum PV power is currently set to 3.3 kW. These values can be adjusted to modify the PV power curve.
- This workflow covers the time period of 24 hours, starting at midnight. The power values of the meter and the PV simulator are defined in 10 minute steps, starting at 00:00, 00:10 and so on. The last time point is 23:50.
- The meter sequence reads the PV_QUEUE/Queue/Input/measure_time_points.csv file and defines 144 random power values within the range of 0 - 9 kW for every time step. Each time - power pair of values is sent to the broker queue one by one, using RabbitMQ. The used host is set to "localhost"
- Simultaneously the PvSimulator code is executed. This launches the RabbitMQ consumer. This receives all pairs of values and stops consuming, once it received 144 messages.
- The PV Simulator creates a power curve from 0 kW during the night, up to the predefined PV maximum power. Between sunrise and sunset, the code uses a Gaussian distribution to simulate the PV power curve. Before sunrise and after sunset it ramps the curve during the twilight time period from 0 W to the start / end point of the Gaussian power curve.
- The PV Simulator adds the PV power curve to the received meter curve and writes the time points, the meter curve, the PV curve and the total sum curve to the file PV_QUEUE/Queue/Output/results.csv, using 4 columns.