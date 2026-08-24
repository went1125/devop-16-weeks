$ErrorActionPreference = 'Stop'

Write-Host '1/4 Validate resolved Compose configuration'
docker compose config --quiet

Write-Host '2/4 Check container state'
$services = docker compose ps --services --filter status=running
$expected = @('gateway', 'frontend', 'api', 'postgres', 'redis')
foreach ($service in $expected) {
    if ($services -notcontains $service) { throw "Service is not running: $service" }
}

Write-Host '3/4 Check gateway and API request path'
$health = Invoke-RestMethod -Uri 'http://localhost:8080/healthz'
if ($health -ne 'ok') { throw "Unexpected gateway health response: $health" }
$info = Invoke-RestMethod -Uri 'http://localhost:8080/api/info'
if ($info.message -ne 'Week 1 stack is running') { throw 'Unexpected API response' }

Write-Host '4/4 Verify API runs as non-root'
$uid = docker compose exec -T api id -u
if ($uid.Trim() -eq '0') { throw 'API is running as root' }

Write-Host "PASS: request path works; API uid=$($uid.Trim()); postgres_visits=$($info.postgres_visits); redis_visits=$($info.redis_visits)" -ForegroundColor Green

