# For registration:

valid_reg = {"email": "eve.holt@reqres.in", "password": "pistol"}

invalid_reg = [{"email": "eve.holt@reqres.in"}, 
{"password": "pistol"}, 
{"email": "eve.holt@reqres.in", "password": " "},
 {"email": " ", "password": "pistol"},
 {"email": " ", "password": " "},
 {"email": "qwerty@reqres.in", "password": "pistol"},
 {"email": "qwerty", "password": "123"}
 ]

reg_schema = {"type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "id",
        "token"
    ],
    "properties": {
        "id": {
            "type": "integer",
            "default": 0,
            "title": "The id Schema",
            "examples": [
                4
            ]
        },
        "token": {
            "type": "string",
            "default": "",
            "title": "The token Schema",
            "examples": [
                "QpwL5tke4Pnpja7X4"
            ]
        }
    },
    "examples": [{
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }]
}

# For login:
valid_login = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

invalid_login = [{"email": "eve.holt@reqres.in"}, 
{"password": "pistol"}, 
{"email": "eve.holt@reqres.in", "password": " "},
 {"email": " ", "password": "pistol"},
 {"email": " ", "password": " "},
 {"email": "qwerty@reqres.in", "password": "pistol"},
 {"email": "qwerty", "password": "123"},
 {"email": "eve.holt@reqres.in", "password": "qwerty"}
 ]

login_schema = {"type": "object",
    "required": [
        "token"
    ],
    "properties": {
        "token": {
            "type": "string",
            "default": "",
            "title": "The token Schema"
        }
    }
}

# For users:
valid_user = {
    "name": "morpheus",
    "job": "leader"
}

update_user = {
    "name": "morpheus",
    "job": "zion resident"
}

create_user_schema = {
    "name": "morpheus",
    "job": "leader",
    "id": "104",
    "createdAt": "2022-06-20T17:48:39.795Z"
}

update_user_schema = {
    "type": "object",
    "required": [
        "name",
        "job",
        "updatedAt"
    ],
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    }
}

get_users_schema = {
    "type": "object",
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ],
    "properties": {
        "page": {
            "type": "number"
        },
        "per_page": {
            "type": "number"
        },
        "total": {
            "type": "number"
        },
        "total_pages": {
            "type": "number"
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"
                ],
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "email": {
                        "type": "string"
                    },
                    "first_name": {
                        "type": "string"
                    },
                    "last_name": {
                        "type": "string"
                    },
                    "avatar": {
                        "type": "string"
                    }
                }
            }
        },
        "support": {
            "type": "object",
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
}

single_user_schema = {
    "type": "object",
    "required": [
        "data",
        "support"
    ],
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "id",
                "email",
                "first_name",
                "last_name",
                "avatar"
            ],
            "properties": {
                "id": {
                    "type": "number"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            }
        },
        "support": {
            "type": "object",
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
}