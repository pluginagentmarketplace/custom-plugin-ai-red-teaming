#!/bin/bash
# LLM Infrastructure Security Audit Script
# Checks common security configurations

echo "========================================"
echo "LLM Infrastructure Security Audit"
echo "========================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0
WARNINGS=0

check_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((PASSED++))
}

check_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    ((FAILED++))
}

check_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    ((WARNINGS++))
}

# 1. Check if running as root (should not be)
echo "=== Process Security ==="
if [ "$EUID" -eq 0 ]; then
    check_fail "Running as root - should use non-privileged user"
else
    check_pass "Running as non-root user"
fi

# 2. Check environment variables for secrets
echo ""
echo "=== Environment Security ==="
if env | grep -iE "(api_key|secret|password|token)" > /dev/null 2>&1; then
    check_warn "Sensitive environment variables detected"
else
    check_pass "No obvious secrets in environment"
fi

# 3. Check for .env files
if [ -f ".env" ]; then
    check_warn ".env file exists - ensure not in version control"
else
    check_pass "No .env file in current directory"
fi

# 4. Check file permissions
echo ""
echo "=== File Permissions ==="
if [ -d "./config" ]; then
    perms=$(stat -f "%Lp" ./config 2>/dev/null || stat -c "%a" ./config 2>/dev/null)
    if [ "$perms" = "700" ] || [ "$perms" = "750" ]; then
        check_pass "Config directory has restrictive permissions"
    else
        check_warn "Config directory permissions: $perms (recommend 700 or 750)"
    fi
fi

# 5. Check for open ports (basic)
echo ""
echo "=== Network Security ==="
if command -v netstat &> /dev/null; then
    listening=$(netstat -an 2>/dev/null | grep LISTEN | wc -l)
    echo "Listening ports: $listening"
    if [ "$listening" -gt 10 ]; then
        check_warn "Many listening ports ($listening) - review necessity"
    else
        check_pass "Reasonable number of listening ports"
    fi
fi

# 6. Check for Docker security
echo ""
echo "=== Container Security ==="
if command -v docker &> /dev/null; then
    if docker info 2>/dev/null | grep -q "rootless"; then
        check_pass "Docker running in rootless mode"
    else
        check_warn "Docker not in rootless mode"
    fi
fi

# Summary
echo ""
echo "========================================"
echo "AUDIT SUMMARY"
echo "========================================"
echo -e "Passed:   ${GREEN}$PASSED${NC}"
echo -e "Failed:   ${RED}$FAILED${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

if [ $FAILED -gt 0 ]; then
    echo "Status: FAILED - Address critical issues"
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo "Status: PASSED WITH WARNINGS - Review recommendations"
    exit 0
else
    echo "Status: PASSED"
    exit 0
fi
