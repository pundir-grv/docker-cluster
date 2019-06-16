//replica.js
rs.initiate({
 _id: 'akatsuki',
 members: [
	 	{_id: 0, host: 'mongo1:27017', votes: 1, priority: 2 },
	 	{_id: 1, host: 'mongo2:27017', votes: 1, priority: 1 },
	 	{_id: 2, host: 'mongo3:27017', votes: 1, priority: 1 },
	 	{_id: 3, host: 'mongo4:27017', arbiterOnly: true },
	 	{_id: 4, host: 'mongo5:27017', votes: 0, priority: 0, hidden: true, slaveDelay: 300 }
 ]
})
