url="http://localhost:8081/longtask"

curl -s -X POST \
  -H "content-type: application/json" \
  -w " %{http_code}" \
  -D - \
  "$url"
