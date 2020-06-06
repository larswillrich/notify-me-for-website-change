# notify-me-for-website-change

Crate a file called `config.json` in the folder and run the run.sh:  

```
{
    "smtp":{
        "senderEmail": "senderEmail@example.com",
        "password": "password",
        "endpoint": "smtp.server.com",
        "receiverEmail": "receiverEmail@example.com",
        "message": "Found it! Yeah!"
    },
    "URLs":[
        "https://www.facebook.com/",
        "https://www.google.de/",
        "https://www.amazon.com/"
    ],
    "search":{
        "attr": {
            "Name": "class",
            "Value": "please-find-me"
        },
        "contains": "I am inside the tag"
    }
}
```