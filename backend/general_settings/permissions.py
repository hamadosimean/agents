from rest_framework import permissions
from accounts.models import UserRole, Role


class IsOwner(permissions.BasePermission):
    """Allow access only to the owner of the object"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.user_role.filter(role__name="user").exists()
        )

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return obj.user == request.user
        return False


class IsDriver(permissions.BasePermission):
    """Allow access only to verified drivers"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has driver role
        has_role = request.user.user_role.filter(role__name="driver").exists()

        # Check if user has verified driver profile
        driver_profile = getattr(request.user, "driver", None)
        is_verified = driver_profile.is_verified if driver_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        # Allow if the object belongs to the user
        if hasattr(obj, "user"):
            return obj.user == request.user
        return False


class IsManager(permissions.BasePermission):
    """Allow access only to verified managers"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        # Check if user has manager role
        has_role = request.user.user_role.filter(role__name="manager").exists()

        # Check if user has verified manager profile
        manager_profile = getattr(request.user, "manager", None)
        is_verified = manager_profile.is_verified if manager_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        # Object belongs to the user
        if hasattr(obj, "user"):
            return obj.user == request.user
        return request.user.is_superuser


class IsAdminOrManager(permissions.BasePermission):
    """Allow access only to admin or manager"""

    def has_permission(self, request, view):
        return (
            request.user.is_superuser
            or request.user.user_role.filter(role__name="manager").exists()
            or request.user.user_role.filter(role__name="admin").exists()
        )


class IsManagerDriver(permissions.BasePermission):
    """Allow access only to the manager of the car"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has manager role
        has_role = request.user.user_role.filter(role__name="manager").exists()

        # Check if user has verified manager profile
        manager_profile = getattr(request.user, "manager", None)
        is_verified = manager_profile.is_verified if manager_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "car_driver"):
            manager_profile = getattr(request.user, "manager", None)
            if manager_profile and obj.car_driver.car.manager == manager_profile:
                return True
        return False


class IsManagerCar(permissions.BasePermission):
    """Allow access only to the manager of the car"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has manager role
        has_role = request.user.user_role.filter(role__name="manager").exists()

        # Check if user has verified manager profile
        manager_profile = getattr(request.user, "manager", None)
        is_verified = manager_profile.is_verified if manager_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "manager"):
            manager_profile = getattr(request.user, "manager", None)
            if manager_profile and obj.manager == manager_profile:
                return True
        return False


class IsDriverCar(permissions.BasePermission):
    """Allow access only to the driver of the car"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has driver role
        has_role = request.user.user_role.filter(role__name="driver").exists()

        # Check if user has verified driver profile
        driver_profile = getattr(request.user, "driver", None)
        is_verified = driver_profile.is_verified if driver_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        # Verify if the user (driver) is assigned to this car
        if hasattr(obj, "car_driver"):
            driver_profile = getattr(request.user, "driver", None)
            if driver_profile:
                return obj.car_driver.filter(driver=driver_profile).exists()
        return False


class IsManagerCarDriver(permissions.BasePermission):
    """Allow access only to the manager or driver of the car"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has manager or driver role
        has_role = (
            request.user.user_role.filter(role__name="manager").exists()
            or request.user.user_role.filter(role__name="driver").exists()
        )

        # Check if user has verified manager or driver profile
        manager_profile = getattr(request.user, "manager", None)
        is_verified = manager_profile.is_verified if manager_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "car"):
            manager_profile = getattr(request.user, "manager", None)
            if manager_profile and obj.car.manager == manager_profile:
                return True
        return False


class IsManagerAssuranceOrMaintenance(permissions.BasePermission):
    """Allow access only to the manager of the assurance or maintenance"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has manager role
        has_role = request.user.user_role.filter(role__name="manager").exists()

        # Check if user has verified manager profile
        manager_profile = getattr(request.user, "manager", None)
        is_verified = manager_profile.is_verified if manager_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        # Determine the manager of the car related to the object
        car = getattr(obj, "car", None)
        if car:
            manager_profile = getattr(request.user, "manager", None)
            if manager_profile and car.manager == manager_profile:
                return True
        return False


# driver ride
class IsDriverRide(permissions.BasePermission):
    """Allow access only to the driver of the ride"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Check if user has driver role
        has_role = request.user.user_role.filter(role__name="driver").exists()

        # Check if user has verified driver profile
        driver_profile = getattr(request.user, "driver", None)
        is_verified = driver_profile.is_verified if driver_profile else False

        return has_role and is_verified

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "car_driver"):
            driver_profile = getattr(request.user, "driver", None)
            if driver_profile:
                return obj.car_driver.driver == driver_profile
        return False


# ride review
class IsRideReviewer(permissions.BasePermission):
    """Allow access only to the reviewer of the ride"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        # Verify if the user (driver) is assigned to this ride
        if hasattr(obj, "ride"):
            ride = obj.ride
            if ride.user == request.user:
                return True
        return False
