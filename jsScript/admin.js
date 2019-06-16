// admin.js
admin = db.getSiblingDB("admin")
// creation of the admin user
admin.createUser(
  {
    user: "itachi",
    pwd: "amaterasu",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
// let's authenticate to create the other user
db.getSiblingDB("admin").auth("itachi", "amaterasu" )
// creation of the replica set admin user
db.getSiblingDB("admin").createUser(
  {
    "user" : "nagato",
    "pwd" : "shinratensei",
    roles: [ { "role" : "clusterAdmin", "db" : "admin" } ]
  }
)
