// run `npx shadcn@latest add "https://r.assistant-ui.com/assistant-modal"`
 
import { AssistantRuntimeProvider } from "@assistant-ui/react";
import { useChatRuntime } from "@assistant-ui/react-ai-sdk";
import { AssistantModal } from "@/components/assistant-ui/assistant-modal";
 
const MyApp = () => {
  const runtime = useChatRuntime({
    api: "/api/chat",
  });
 
  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <AssistantModal />
    </AssistantRuntimeProvider>
  );
};