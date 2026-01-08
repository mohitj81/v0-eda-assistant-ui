"use client"

import type React from "react"
import { createContext, useContext, useState, useCallback } from "react"
import type { EDAState } from "./types"
import { apiClient } from "./api-client"

interface EDAContextType extends EDAState {
  uploadDataset: (file: File) => Promise<void>
  fetchProfilingResults: (sessionId: string) => Promise<void>
  fetchRiskAssessment: (sessionId: string) => Promise<void>
  fetchExplanation: (sessionId: string) => Promise<void>
  fetchCleaningScript: (sessionId: string) => Promise<void>
  fetchComparison: (sessionId: string) => Promise<void>
  resetState: () => void
}

const EDAContext = createContext<EDAContextType | undefined>(undefined)

export function EDAProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<EDAState>({
    currentDataset: null,
    profiling: null,
    riskAssessment: null,
    cleaningScript: null,
    explanation: null,
    comparison: null,
    loading: false,
    error: null,
  })

  const uploadDataset = useCallback(async (file: File) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.uploadDataset(file)
      setState((prev) => ({
        ...prev,
        currentDataset: {
          id: result.session_id,
          filename: result.filename,
          size: file.size,
          uploadedAt: new Date(),
          rows: result.rows,
          columns: result.columns,
        },
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to upload dataset",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const fetchProfilingResults = useCallback(async (sessionId: string) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.getProfilingResults(sessionId)
      setState((prev) => ({
        ...prev,
        profiling: result,
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to fetch profiling results",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const fetchRiskAssessment = useCallback(async (sessionId: string) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.getRiskAssessment(sessionId)
      setState((prev) => ({
        ...prev,
        riskAssessment: result,
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to fetch risk assessment",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const fetchExplanation = useCallback(async (sessionId: string) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.getExplanation(sessionId)
      setState((prev) => ({
        ...prev,
        explanation: result,
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to fetch explanation",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const fetchCleaningScript = useCallback(async (sessionId: string) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.getCleaningScript(sessionId)
      setState((prev) => ({
        ...prev,
        cleaningScript: {
          code: result,
          language: "python",
          format: "pandas",
        },
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to fetch cleaning script",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const fetchComparison = useCallback(async (sessionId: string) => {
    setState((prev) => ({ ...prev, loading: true, error: null }))
    try {
      const result = await apiClient.getComparison(sessionId)
      setState((prev) => ({
        ...prev,
        comparison: result,
      }))
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : "Failed to fetch comparison",
      }))
    } finally {
      setState((prev) => ({ ...prev, loading: false }))
    }
  }, [])

  const resetState = useCallback(() => {
    setState({
      currentDataset: null,
      profiling: null,
      riskAssessment: null,
      cleaningScript: null,
      explanation: null,
      comparison: null,
      loading: false,
      error: null,
    })
  }, [])

  return (
    <EDAContext.Provider
      value={{
        ...state,
        uploadDataset,
        fetchProfilingResults,
        fetchRiskAssessment,
        fetchExplanation,
        fetchCleaningScript,
        fetchComparison,
        resetState,
      }}
    >
      {children}
    </EDAContext.Provider>
  )
}

export function useEDA() {
  const context = useContext(EDAContext)
  if (!context) {
    throw new Error("useEDA must be used within an EDAProvider")
  }
  return context
}
