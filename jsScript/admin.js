// admin.js
admin = db.getSiblingDB("admin")
// creation of the admin user
admin.createUser(
  {
    user: "itachi",
    pwd: "amaterasu",
    roles: [ "userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase", "clusterAdmin" ]
  }
)

