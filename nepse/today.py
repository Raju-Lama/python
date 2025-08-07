import json

# Replace the triple quotes below with your full JSON data
json_data = """
{
    "data": [{
  "totalCount": 93122,
  "totalPages": 1863,
  "currentPage": 1,
  "data": [
    {
      "serialNumber": 1,
      "contractNumber": 2025080601000001,
      "stockSymbol": "SBI",
      "buyerBroker": 34,
      "sellerBroker": 48,
      "quantity": 10,
      "rate": 426.8,
      "amount": 4268,
      "timestamp": "2025-08-06 10:46:00.011148"
    },
    {
      "serialNumber": 2,
      "contractNumber": 2025080601000002,
      "stockSymbol": "KBL",
      "buyerBroker": 93,
      "sellerBroker": 55,
      "quantity": 10,
      "rate": 220,
      "amount": 2200,
      "timestamp": "2025-08-06 10:46:00.020375"
    },
    {
      "serialNumber": 3,
      "contractNumber": 2025080601000003,
      "stockSymbol": "SBL",
      "buyerBroker": 29,
      "sellerBroker": 11,
      "quantity": 10,
      "rate": 380.6,
      "amount": 3806,
      "timestamp": "2025-08-06 10:46:00.023010"
    },
    {
      "serialNumber": 4,
      "contractNumber": 2025080601000004,
      "stockSymbol": "PRVU",
      "buyerBroker": 34,
      "sellerBroker": 55,
      "quantity": 10,
      "rate": 236.2,
      "amount": 2362,
      "timestamp": "2025-08-06 10:46:00.030671"
    },
    {
      "serialNumber": 5,
      "contractNumber": 2025080601000005,
      "stockSymbol": "GBIME",
      "buyerBroker": 56,
      "sellerBroker": 44,
      "quantity": 10,
      "rate": 260.5,
      "amount": 2605,
      "timestamp": "2025-08-06 10:46:00.032479"
    },
    {
      "serialNumber": 6,
      "contractNumber": 2025080601000006,
      "stockSymbol": "CZBIL",
      "buyerBroker": 34,
      "sellerBroker": 55,
      "quantity": 10,
      "rate": 226.8,
      "amount": 2268,
      "timestamp": "2025-08-06 10:46:00.034972"
    },
    {
      "serialNumber": 7,
      "contractNumber": 2025080601000007,
      "stockSymbol": "ADBL",
      "buyerBroker": 34,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 331.8,
      "amount": 3318,
      "timestamp": "2025-08-06 10:46:00.037820"
    },
    {
      "serialNumber": 8,
      "contractNumber": 2025080601000008,
      "stockSymbol": "SAMAJ",
      "buyerBroker": 34,
      "sellerBroker": 22,
      "quantity": 10,
      "rate": 2803.1,
      "amount": 28031,
      "timestamp": "2025-08-06 10:46:00.072468"
    },
    {
      "serialNumber": 9,
      "contractNumber": 2025080601000009,
      "stockSymbol": "SAMAJ",
      "buyerBroker": 34,
      "sellerBroker": 1,
      "quantity": 10,
      "rate": 2803.1,
      "amount": 28031,
      "timestamp": "2025-08-06 10:46:00.072525"
    },
    {
      "serialNumber": 10,
      "contractNumber": 2025080601000010,
      "stockSymbol": "SRLI",
      "buyerBroker": 34,
      "sellerBroker": 62,
      "quantity": 10,
      "rate": 418.6,
      "amount": 4186,
      "timestamp": "2025-08-06 10:46:00.075617"
    },
    {
      "serialNumber": 11,
      "contractNumber": 2025080601000011,
      "stockSymbol": "CITY",
      "buyerBroker": 34,
      "sellerBroker": 55,
      "quantity": 10,
      "rate": 945.7,
      "amount": 9457,
      "timestamp": "2025-08-06 10:46:00.111988"
    },
    {
      "serialNumber": 12,
      "contractNumber": 2025080601000012,
      "stockSymbol": "SNLI",
      "buyerBroker": 56,
      "sellerBroker": 48,
      "quantity": 10,
      "rate": 492.7,
      "amount": 4927,
      "timestamp": "2025-08-06 10:46:00.122296"
    },
    {
      "serialNumber": 13,
      "contractNumber": 2025080601000013,
      "stockSymbol": "MKCL",
      "buyerBroker": 42,
      "sellerBroker": 34,
      "quantity": 10,
      "rate": 1638.3,
      "amount": 16383,
      "timestamp": "2025-08-06 10:46:00.126476"
    },
    {
      "serialNumber": 14,
      "contractNumber": 2025080601000014,
      "stockSymbol": "NICGF2",
      "buyerBroker": 40,
      "sellerBroker": 20,
      "quantity": 100,
      "rate": 9.48,
      "amount": 948,
      "timestamp": "2025-08-06 10:46:00.129589"
    },
    {
      "serialNumber": 15,
      "contractNumber": 2025080601000015,
      "stockSymbol": "PURE",
      "buyerBroker": 6,
      "sellerBroker": 45,
      "quantity": 10,
      "rate": 850,
      "amount": 8500,
      "timestamp": "2025-08-06 10:46:00.148944"
    },
    {
      "serialNumber": 16,
      "contractNumber": 2025080601000016,
      "stockSymbol": "TTL",
      "buyerBroker": 49,
      "sellerBroker": 45,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153491"
    },
    {
      "serialNumber": 17,
      "contractNumber": 2025080601000017,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 45,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153603"
    },
    {
      "serialNumber": 18,
      "contractNumber": 2025080601000018,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 38,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153646"
    },
    {
      "serialNumber": 19,
      "contractNumber": 2025080601000019,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 38,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153676"
    },
    {
      "serialNumber": 20,
      "contractNumber": 2025080601000020,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 34,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153757"
    },
    {
      "serialNumber": 21,
      "contractNumber": 2025080601000021,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 72,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153793"
    },
    {
      "serialNumber": 22,
      "contractNumber": 2025080601000022,
      "stockSymbol": "TTL",
      "buyerBroker": 7,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153821"
    },
    {
      "serialNumber": 23,
      "contractNumber": 2025080601000023,
      "stockSymbol": "TTL",
      "buyerBroker": 26,
      "sellerBroker": 34,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 10:46:00.153850"
    },
    {
      "serialNumber": 24,
      "contractNumber": 2025080601000024,
      "stockSymbol": "TTL",
      "buyerBroker": 62,
      "sellerBroker": 49,
      "quantity": 10,
      "rate": 941,
      "amount": 9410,
      "timestamp": "2025-08-06 10:46:00.221555"
    },
    {
      "serialNumber": 25,
      "contractNumber": 2025080601000025,
      "stockSymbol": "TTL",
      "buyerBroker": 62,
      "sellerBroker": 49,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.221655"
    },
    {
      "serialNumber": 26,
      "contractNumber": 2025080601000026,
      "stockSymbol": "TTL",
      "buyerBroker": 62,
      "sellerBroker": 57,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.221713"
    },
    {
      "serialNumber": 27,
      "contractNumber": 2025080601000027,
      "stockSymbol": "TTL",
      "buyerBroker": 62,
      "sellerBroker": 6,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.221766"
    },
    {
      "serialNumber": 28,
      "contractNumber": 2025080601000028,
      "stockSymbol": "TTL",
      "buyerBroker": 38,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.233234"
    },
    {
      "serialNumber": 29,
      "contractNumber": 2025080601000029,
      "stockSymbol": "TTL",
      "buyerBroker": 38,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.233303"
    },
    {
      "serialNumber": 30,
      "contractNumber": 2025080601000030,
      "stockSymbol": "TTL",
      "buyerBroker": 38,
      "sellerBroker": 49,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 10:46:00.233350"
    },
    {
      "serialNumber": 112,
      "contractNumber": 2025080601000031,
      "stockSymbol": "TTL",
      "buyerBroker": 44,
      "sellerBroker": 91,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 11:00:11.976928"
    },
    {
      "serialNumber": 113,
      "contractNumber": 2025080601000032,
      "stockSymbol": "TTL",
      "buyerBroker": 44,
      "sellerBroker": 38,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 11:00:11.976997"
    },
    {
      "serialNumber": 114,
      "contractNumber": 2025080601000033,
      "stockSymbol": "TTL",
      "buyerBroker": 44,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 11:00:11.977067"
    },
    {
      "serialNumber": 115,
      "contractNumber": 2025080601000034,
      "stockSymbol": "TTL",
      "buyerBroker": 44,
      "sellerBroker": 55,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 11:00:11.977103"
    },
    {
      "serialNumber": 116,
      "contractNumber": 2025080601000035,
      "stockSymbol": "TTL",
      "buyerBroker": 44,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 950,
      "amount": 9500,
      "timestamp": "2025-08-06 11:00:11.977141"
    },
    {
      "serialNumber": 117,
      "contractNumber": 2025080601000036,
      "stockSymbol": "TTL",
      "buyerBroker": 26,
      "sellerBroker": 13,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:12.105653"
    },
    {
      "serialNumber": 118,
      "contractNumber": 2025080601000037,
      "stockSymbol": "TTL",
      "buyerBroker": 26,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:16.841922"
    },
    {
      "serialNumber": 119,
      "contractNumber": 2025080601000038,
      "stockSymbol": "TTL",
      "buyerBroker": 26,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:17.976018"
    },
    {
      "serialNumber": 120,
      "contractNumber": 2025080601000039,
      "stockSymbol": "TTL",
      "buyerBroker": 26,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:19.684098"
    },
    {
      "serialNumber": 121,
      "contractNumber": 2025080601000040,
      "stockSymbol": "TTL",
      "buyerBroker": 43,
      "sellerBroker": 34,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:22.176245"
    },
    {
      "serialNumber": 122,
      "contractNumber": 2025080601000041,
      "stockSymbol": "TTL",
      "buyerBroker": 43,
      "sellerBroker": 58,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:22.757586"
    },
    {
      "serialNumber": 123,
      "contractNumber": 2025080601000042,
      "stockSymbol": "TTL",
      "buyerBroker": 43,
      "sellerBroker": 62,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:22.801009"
    },
    {
      "serialNumber": 124,
      "contractNumber": 2025080601000043,
      "stockSymbol": "TTL",
      "buyerBroker": 58,
      "sellerBroker": 32,
      "quantity": 10,
      "rate": 941,
      "amount": 9410,
      "timestamp": "2025-08-06 11:00:24.526367"
    },
    {
      "serialNumber": 125,
      "contractNumber": 2025080601000044,
      "stockSymbol": "TTL",
      "buyerBroker": 43,
      "sellerBroker": 91,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:25.614567"
    },
    {
      "serialNumber": 126,
      "contractNumber": 2025080601000045,
      "stockSymbol": "SAMAJ",
      "buyerBroker": 34,
      "sellerBroker": 1,
      "quantity": 29,
      "rate": 2803.1,
      "amount": 81289,
      "timestamp": "2025-08-06 11:00:26.233211"
    },
    {
      "serialNumber": 127,
      "contractNumber": 2025080601000046,
      "stockSymbol": "TTL",
      "buyerBroker": 43,
      "sellerBroker": 45,
      "quantity": 10,
      "rate": 940,
      "amount": 9400,
      "timestamp": "2025-08-06 11:00:26.729827"
    },
    {
      "serialNumber": 128,
      "contractNumber": 2025080601000047,
      "stockSymbol": "PCBL",
      "buyerBroker": 56,
      "sellerBroker": 10,
      "quantity": 400,
      "rate": 258.29,
      "amount": 103316,
      "timestamp": "2025-08-06 11:00:27.044917"
    },
    {
      "serialNumber": 129,
      "contractNumber": 2025080601000048,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 49,
      "quantity": 10,
      "rate": 940.3,
      "amount": 9403,
      "timestamp": "2025-08-06 11:00:31.315140"
    },
    {
      "serialNumber": 130,
      "contractNumber": 2025080601000049,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 19,
      "quantity": 10,
      "rate": 941,
      "amount": 9410,
      "timestamp": "2025-08-06 11:00:32.865125"
    },
    {
      "serialNumber": 131,
      "contractNumber": 2025080601000050,
      "stockSymbol": "TTL",
      "buyerBroker": 57,
      "sellerBroker": 41,
      "quantity": 10,
      "rate": 941,
      "amount": 9410,
      "timestamp": "2025-08-06 11:00:33.594342"
    }
  ]
}
}
"""

# Save it to a file
with open("floorsheet_data.json", "w") as f:
    f.write(json_data)

print("floorsheet_data.json created successfully!")