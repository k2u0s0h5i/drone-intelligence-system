from mcp_server.roi_calculator import calculate_roi
from mcp_server.flight_time_estimator import estimate_flight_time
from mcp_server.compliance_checker import check_compliance

print("ROI Test:")
print(calculate_roi(50))

print("\nFlight Time Test:")
print(estimate_flight_time(70))

print("\nCompliance Test:")
print(check_compliance(5, "yellow"))
