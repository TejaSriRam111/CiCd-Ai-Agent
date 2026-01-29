import yaml

def generate_pipeline(tech):
    if tech["language"] == "java" and tech["build_tool"] == "maven":
        pipeline = {
            "name": "Java CI",
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"uses": "actions/checkout@v4"},
                        {
                            "uses": "actions/setup-java@v4",
                            "with": {
                                "java-version": "17",
                                "distribution": "temurin"
                            }
                        },
                        {"run": "mvn clean test package"}
                    ]
                }
            }
        }

    elif tech["language"] == "node":
        pipeline = {
            "name": "Node CI",
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"uses": "actions/checkout@v4"},
                        {"uses": "actions/setup-node@v4", "with": {"node-version": "18"}},
                        {"run": "npm install"},
                        {"run": "npm test || true"}
                    ]
                }
            }
        }

    elif tech["language"] == "python":
        pipeline = {
            "name": "Python CI",
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"uses": "actions/checkout@v4"},
                        {"run": "pip install -r requirements.txt"},
                        {"run": "pytest || true"}
                    ]
                }
            }
        }

    # ✅ ADD THIS BLOCK (STATIC HTML SUPPORT)
    elif tech["language"] == "html":
        pipeline = {
            "name": "Static Site CI",
            "on": ["push"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": [
                        {"uses": "actions/checkout@v4"},
                        {"run": "echo 'Static HTML site - no build required'"}
                    ]
                }
            }
        }

    else:
        pipeline = {
            "error": "Unsupported project"
        }

    return yaml.dump(pipeline, sort_keys=False)
