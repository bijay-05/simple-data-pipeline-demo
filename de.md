import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.route_params.get('name')
    return func.HttpResponse(f"Hello, {name}",status_code=200)




  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get",
        "post"
      ],
      "route": "dynamichost/{name}"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
