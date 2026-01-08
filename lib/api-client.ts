// API client for communicating with the backend

const API_BASE_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000"

export const apiClient = {
  async uploadDataset(file: File): Promise<{
    success: boolean
    session_id: string
    filename: string
    rows: number
    columns: number
    column_names: string[]
    preview: Record<string, any>[]
  }> {
    const formData = new FormData()
    formData.append("file", file)

    const response = await fetch(`${API_BASE_URL}/upload`, {
      method: "POST",
      body: formData,
    })

    if (!response.ok) {
      throw new Error("Failed to upload dataset")
    }

    return response.json()
  },

  async getProfilingResults(sessionId: string): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/profile?session_id=${encodeURIComponent(sessionId)}`)
    if (!response.ok) {
      throw new Error("Failed to fetch profiling results")
    }
    return response.json()
  },

  async getRiskAssessment(sessionId: string): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/risk?session_id=${encodeURIComponent(sessionId)}`)
    if (!response.ok) {
      throw new Error("Failed to fetch risk assessment")
    }
    return response.json()
  },

  async getExplanation(sessionId: string): Promise<string> {
    const response = await fetch(`${API_BASE_URL}/explain?session_id=${encodeURIComponent(sessionId)}`)
    if (!response.ok) {
      throw new Error("Failed to fetch explanation")
    }
    const data = await response.json()
    return data.explanation
  },

  async getCleaningScript(sessionId: string): Promise<string> {
    const response = await fetch(`${API_BASE_URL}/script?session_id=${encodeURIComponent(sessionId)}`)
    if (!response.ok) {
      throw new Error("Failed to fetch cleaning script")
    }
    const data = await response.json()
    return data.script
  },

  async getComparison(sessionId: string): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/compare?session_id=${encodeURIComponent(sessionId)}`)
    if (!response.ok) {
      throw new Error("Failed to fetch comparison")
    }
    return response.json()
  },

  async healthCheck(): Promise<{ status: string; version: string }> {
    const response = await fetch(`${API_BASE_URL}/health`)
    if (!response.ok) {
      throw new Error("Backend is not available")
    }
    return response.json()
  },
}
