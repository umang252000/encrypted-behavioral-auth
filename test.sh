#!/usr/bin/env bash
set -e

# ============================
# CONFIG
# ============================

BASE_URL="https://fuzzy-happiness-4qgrrvw46jv2vj7-8000.app.github.dev"

ADMIN_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbi0xIiwicm9sZSI6ImFkbWluIiwidGVuYW50Ijoib3JnLTEiLCJleHAiOjE3NjY3MzMwOTJ9.BYXEvAqEMSN5sWmAbpyfe6hPUbaLWF4wvaePnR3VU9M"

USER_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyLTEiLCJyb2xlIjoidXNlciIsInRlbmFudCI6Im9yZy0xIiwiZXhwIjoxNzY2NzMzMDkyfQ.Y3rPtZj7xbwJgTLTM9r6mzxLler-iRGTN5AK3PwwXlA"

CIPHERTEXT="c41ed70ac3bd232f0c9c4816c18354cf4dec8596cf8c694a630f88ac391d1bd262c5cabb5bd31e6a714999cc54e2482ea3bfd89dcd243fe1206b36996e25b577875f177745f1fb829958a7e11cfeadb24815184a2bf405e119c050ebbdcabdb1505e4dddedcb9e814df0ce39677fc155cdbbaa5a499f6280a069ec90d50db8e612ee06f143c8c904dac16ff58ded652beeba50cea3541c45439a2569b9f436a930186a685b64f8a0d177441acec8fc520d30388b0e759c4519b33c9db0f735ec76cba718ebaabc71eff4ed9e49898ea811b08bc3bd4fbc6d2d8c7ce552a6ed471db3bc529ea22786e7c452d170fa767d8fadc2175cebce6d71bb64acb714fcd9a0917458b0a2d79c6b5e6a16e993762a87315af3c3b91ce53fb33057bf423fc07c6e6d313c8bc2d8d1fe3b56d5067f1b801bbce4f9b5f4274f8ea10142139c38f8d1728e4268ba8f9bdabdba45253939ead9a83acc6256e7f274d602f4fdf20603a0087e202f728595cc3de920819361f332f87729ff02009a8f0cee2312a10d7c3087f4886576bd51d114e3e44b42afa431e54044aad6f1e17ab187414b9711d55de3d964e95e3980c35f85d44258ee9efc06962472e5f8c63b3cf9ef4a3d583e2fce38857fd63498204e2652ebd885c9c524e4a12deb9161e1db936ca533cc3eb3c46a1eea76a7e6621f0ec740009b3d8e8cf68cb8277a9f884d783b0c05d3aa3edfd2839410bc63bd37db10455579"

NONCE="126e0eb26e6388667ce4d502"

# ============================
# HELPERS
# ============================

divider () {
  echo
  echo "===================================================="
  echo "$1"
  echo "===================================================="
}

# ============================
# TESTS
# ============================

divider "TEST 1 — HEALTH CHECK"
curl -s "$BASE_URL/health"
echo

divider "TEST 2 — REGISTER (ADMIN)"
curl -s -X POST "$BASE_URL/register" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"user_id\": \"user-1\",
    \"encrypted_embedding\": {
      \"ciphertext\": \"$CIPHERTEXT\",
      \"nonce\": \"$NONCE\"
    }
  }"
echo

divider "TEST 3 — REGISTER (USER → SHOULD FAIL)"
curl -s -X POST "$BASE_URL/register" \
  -H "Authorization: Bearer $USER_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{}"
echo

divider "TEST 4 — LOGIN (CORE SUCCESS)"
curl -s -X POST "$BASE_URL/login" \
  -H "Authorization: Bearer $USER_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"encrypted_embedding\": {
      \"ciphertext\": \"$CIPHERTEXT\",
      \"nonce\": \"$NONCE\"
    }
  }"
echo

divider "TEST 5 — LOGIN (NO TOKEN → SHOULD FAIL)"
curl -s -X POST "$BASE_URL/login" \
  -H "Content-Type: application/json" \
  -d "{}"
echo

divider "TEST 6 — METRICS (ADMIN)"
curl -s "$BASE_URL/metrics" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
echo

divider "TEST 7 — METRICS (USER → SHOULD FAIL)"
curl -s "$BASE_URL/metrics" \
  -H "Authorization: Bearer $USER_TOKEN"
echo

divider "ALL TESTS COMPLETED"