from django.db import models

class Well(models.Model):
    name = models.CharField(max_length=255)
    well_id = models.CharField(max_length=255, blank=True, default="")
    location = models.CharField(max_length=255, blank=True, default="")
    well_type = models.CharField(max_length=50, choices=[("production", "Production"), ("injection", "Injection"), ("exploration", "Exploration"), ("observation", "Observation")], default="production")
    depth_m = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("shut_in", "Shut In"), ("abandoned", "Abandoned"), ("drilling", "Drilling")], default="active")
    daily_output = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    spud_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Production(models.Model):
    well_name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    oil_bbl = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gas_mcf = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    water_bbl = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    uptime_hours = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("normal", "Normal"), ("low", "Low"), ("shutdown", "Shutdown")], default="normal")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.well_name

class OGEquipment(models.Model):
    name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=50, choices=[("pump", "Pump"), ("compressor", "Compressor"), ("separator", "Separator"), ("generator", "Generator"), ("valve", "Valve")], default="pump")
    serial_number = models.CharField(max_length=255, blank=True, default="")
    well_name = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("operational", "Operational"), ("maintenance", "Maintenance"), ("failed", "Failed")], default="operational")
    last_service = models.DateField(null=True, blank=True)
    next_service = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
