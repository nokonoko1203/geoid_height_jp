# geoid

This is AWS lambda function of calculating Geoid Height from Japan geoid model.
Input lat/lng of JGD2011, Then getting geoid Height.

## setup

Before the next `install` step then install AWS CLI, Serverless Framework, and configure AWS CLI.

### install

```shell
% cd function/
% pipenv install
% npm install
```

### deploy

```shell
% sls deploy
```

## run of local function

```shell
% pwd
.../geoid/function
% pipenv install
% sls invoke local -f geoid -d '{"queryStringParameters":{"lat": 34.290, "lng": 135.630}}'
{
    "statusCode": 200,
    "body": "{\"geoid_height\": 39.8601222393958}"
}
```

## run of function

You can run after deploy.

```shell
% sls invoke -f geoid -d '{"queryStringParameters":{"lat": 34.290, "lng": 135.630}}'
{
    "statusCode": 200,
    "body": "{\"geoid_height\": 39.8601222393958}"
}
```