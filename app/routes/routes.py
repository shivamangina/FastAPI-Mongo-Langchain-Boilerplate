from fastapi import APIRouter

from app.routes.endpoints.auth import router as auth_router
from app.routes.endpoints.comments import router as comments_router
from app.routes.endpoints.user import router as user_router
from app.routes.endpoints.health import router as health_router
from app.routes.endpoints.feedback import router as feedback_router

routers = APIRouter()
router_list = [auth_router, comments_router, user_router,health_router, feedback_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)