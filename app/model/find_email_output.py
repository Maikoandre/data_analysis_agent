from pydantic import BaseModel, Field

class FindEmailOutput(BaseModel):
    message_id: str = Field(..., description="The message id of the email")
    thread_id: str = Field(..., description="The thread id of the email")
    references: str = Field(..., description="The references of the email")
    in_reply_to: str = Field(..., description="The in-reply-to of the email")
    subject: str = Field(..., description="The subject of the email")
    body: str = Field(..., description="The body of the email")