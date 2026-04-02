from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Well, Production, OGEquipment
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusOil with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusoil.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Well.objects.count() == 0:
            for i in range(10):
                Well.objects.create(
                    name=f"Sample Well {i+1}",
                    well_id=f"Sample {i+1}",
                    location=f"Sample {i+1}",
                    well_type=random.choice(["production", "injection", "exploration", "observation"]),
                    depth_m=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "shut_in", "abandoned", "drilling"]),
                    daily_output=round(random.uniform(1000, 50000), 2),
                    spud_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Well records created'))

        if Production.objects.count() == 0:
            for i in range(10):
                Production.objects.create(
                    well_name=f"Sample Production {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    oil_bbl=round(random.uniform(1000, 50000), 2),
                    gas_mcf=round(random.uniform(1000, 50000), 2),
                    water_bbl=round(random.uniform(1000, 50000), 2),
                    uptime_hours=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["normal", "low", "shutdown"]),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Production records created'))

        if OGEquipment.objects.count() == 0:
            for i in range(10):
                OGEquipment.objects.create(
                    name=f"Sample OGEquipment {i+1}",
                    equipment_type=random.choice(["pump", "compressor", "separator", "generator", "valve"]),
                    serial_number=f"Sample {i+1}",
                    well_name=f"Sample OGEquipment {i+1}",
                    status=random.choice(["operational", "maintenance", "failed"]),
                    last_service=date.today() - timedelta(days=random.randint(0, 90)),
                    next_service=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 OGEquipment records created'))
