from django.contrib import admin
from .models import Well, Production, OGEquipment

@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = ["name", "well_id", "location", "well_type", "depth_m", "created_at"]
    list_filter = ["well_type", "status"]
    search_fields = ["name", "well_id", "location"]

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ["well_name", "date", "oil_bbl", "gas_mcf", "water_bbl", "created_at"]
    list_filter = ["status"]
    search_fields = ["well_name"]

@admin.register(OGEquipment)
class OGEquipmentAdmin(admin.ModelAdmin):
    list_display = ["name", "equipment_type", "serial_number", "well_name", "status", "created_at"]
    list_filter = ["equipment_type", "status"]
    search_fields = ["name", "serial_number", "well_name"]
