from app.crud.items import expense_crud, budget_crud, goal_crud, invest_crud, income_crud, transaction_crud

expense_router = expense_crud.router

budget_router = budget_crud.router

goal_router = goal_crud.router

income_router = income_crud.router

investment_router = invest_crud.router

transaction_router = transaction_crud.router
