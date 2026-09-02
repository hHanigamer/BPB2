import asyncio
import random
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbtIQpuZYMYoVkWm-4sfOTQA6cKlZDfOOd78TZrTnFNOivlCL-2wYmYB2CMB1QE4D9_rc5NRBuOeFqV2OPsB230ceO2qNxODIqhjbNBsbuh9mJ8L5RFQs6ilz9YzJcbDYMsWhmNPY5idevRfFnporKc7qiHrOmBlbYyixIPs7w-16Rp_BJJLP_tOjwE5MY2SW8VFjNgxnceNk46ui0rfZWR0IxDIQlQrlSKPtx7CdAfwV1PcuCnWU_rnP5c6vbfoY9w4uSP8chReFDmKEPfSligkQ_MxfAXt7-I3vldko_RJ1NEIHo6CBcqHzHwO7rrZ6GF_WYt2_WlSGvp4gxCAUMoG"

async def point_task(client, recipient):
    """Send dot‑messages every 60–70 seconds."""
    ma = alaf = naz = kar = tamiz = shird = shirf = gard = kiss = gaza = bare = 0

    while True:
        await asyncio.sleep(random.uniform(60, 70))
        
        ma += 1
        alaf += 1
        naz += 1
        kar += 1
        tamiz += 1
        shird += 1
        shirf += 1
        gard += 1
        kiss += 1
        gaza += 1
        bare += 1

        if ma >= 5:
            await client.send_message(recipient, 'مع')
            ma = 0
        if alaf >= 7:
            await client.send_message(recipient, 'علف')
            alaf = 0
        if gaza >= 35:
            await client.send_message(recipient, 'غذا بده همه')
            gaza = 0
        if naz >= 9:
            await client.send_message(recipient, 'نازش کن')
            naz = 0
        if tamiz >= 10:
            await client.send_message(recipient, 'تمیزش کن')
            tamiz = 0
        if shird >= 10:
            await client.send_message(recipient, 'شیر بز')
            shird = 0
        if gard >= 10:
            await client.send_message(recipient, 'گردش')
            gard = 0
        if kiss >= 10:
            await client.send_message(recipient, 'بوسش کن')
            kiss = 0
        if bare >= 15:
            await client.send_message(recipient, 'برداشت بره ناقلا')
            bare = 0
        if kar >= 15:
            await client.send_message(recipient, 'جمع آوری کارخانه')
            kar = 0
        if shirf >= 30:
            await client.send_message(recipient, 'فروش شیر')
            shirf = 0

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()
    recipient = "@bozpoint2"   # ⬅️ Replace with actual recipient
    await point_task(client, recipient)

if __name__ == '__main__':
    asyncio.run(main())
