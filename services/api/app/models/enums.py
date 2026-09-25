"""Fixed value sets shared by the database models, API and services."""

from enum import StrEnum


class UserRole(StrEnum):
    CITIZEN = "citizen"
    WORKER = "worker"
    ADMIN = "admin"


class WasteCategory(StrEnum):
    HOUSEHOLD_TRASH = "household_trash"
    GREEN_WASTE = "green_waste"
    CONSTRUCTION_RESIDUE = "construction_residue"
    BULKY_ITEMS = "bulky_items"


class BlindSpotStatus(StrEnum):
    NEW = "new"
    VERIFIED = "verified"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"
    FALSE_POSITIVE = "false_positive"
    DUPLICATE = "duplicate"


class SourceType(StrEnum):
    CITIZEN = "citizen"
    VIRTUAL_CAMERA = "virtual_camera"
    CAMERA = "camera"


class SensitiveSiteType(StrEnum):
    SCHOOL = "school"
    MARKET = "market"
    WATER = "water"
    HEALTH = "health"