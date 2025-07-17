import re

config = "db_host=${DB_HOST : 127.0.0.2} , db_port=${DB_PORT:5432}"

def replace_env_vars(config_str, env):
    return re.sub(
        r'\${(\w+):([^}]+)}',  # Two groups: (\w+) and ([^}]+)
        lambda m: env.get(m.group(1), m.group(2)),  # Use group(2) as default
        config_str
    )

env={
    "DB_HOST":"localhost",
    "${DB_PORT":"5432}"
}

print(replace_env_vars(config,env))

