"use client"

import { Card } from "@/components/ui/card"
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"

const faqItems = [
  {
    question: "What file formats are supported?",
    answer:
      "Currently, EDA Assistant supports CSV (Comma-Separated Values) files. Other formats like Excel, JSON, and Parquet will be added in future releases.",
  },
  {
    question: "How large can my dataset be?",
    answer:
      "Files up to 50MB are supported. For larger datasets, we recommend splitting them into smaller chunks or using our API for programmatic access.",
  },
  {
    question: "What does the risk score mean?",
    answer:
      "The risk score (Low, Medium, High) indicates the overall data quality and potential issues that could impact downstream analysis or machine learning models.",
  },
  {
    question: "Can I use the cleaning script in production?",
    answer:
      "Yes, the generated Python scripts can be integrated into your data pipeline. Ensure you test thoroughly in your environment before production use.",
  },
]

export default function DocumentationPage() {
  return (
    <div className="min-h-screen bg-background p-6 md:p-12">
      <div className="max-w-4xl mx-auto space-y-12">
        {/* Getting Started */}
        <section className="space-y-4">
          <h1 className="text-3xl font-bold">Documentation</h1>
          <p className="text-muted-foreground">Learn how to use EDA Assistant to analyze and clean your data</p>
        </section>

        {/* What is EDA Assistant */}
        <Card className="p-6">
          <h2 className="text-2xl font-bold mb-3">What is EDA Assistant?</h2>
          <p className="text-muted-foreground leading-relaxed">
            EDA Assistant is an automated platform for exploratory data analysis, data quality assessment, and guided
            data cleaning. Upload your CSV file, and the platform will analyze your data structure, identify quality
            issues, assess risks, provide AI-powered insights, and generate Python scripts to clean your data—all in one
            place.
          </p>
        </Card>

        {/* How to Use */}
        <Card className="p-6">
          <h2 className="text-2xl font-bold mb-4">How to Use EDA Assistant</h2>
          <div className="space-y-4">
            <div>
              <h3 className="font-semibold mb-2">1. Upload Your Dataset</h3>
              <p className="text-muted-foreground">
                Go to the Upload page and drag-and-drop your CSV file or browse to select it from your computer.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-2">2. View Data Profiling</h3>
              <p className="text-muted-foreground">
                After upload, review the profiling summary showing column statistics, data types, and unique values.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-2">3. Review Risk Assessment</h3>
              <p className="text-muted-foreground">
                Check the risk assessment page to identify data quality issues and their potential impact.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-2">4. Get AI Insights</h3>
              <p className="text-muted-foreground">
                Review AI-generated explanations of issues found and recommended actions to improve data quality.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-2">5. Download Cleaning Script</h3>
              <p className="text-muted-foreground">
                Get an auto-generated Python script that implements all recommended data cleaning steps.
              </p>
            </div>
            <div>
              <h3 className="font-semibold mb-2">6. Export Reports</h3>
              <p className="text-muted-foreground">
                Download comprehensive reports in PDF, JSON, or other formats for documentation and sharing.
              </p>
            </div>
          </div>
        </Card>

        {/* How to Run the Script */}
        <Card className="p-6">
          <h2 className="text-2xl font-bold mb-4">Running the Python Script</h2>
          <div className="space-y-3 text-muted-foreground">
            <p>1. Ensure you have Python 3.7+ installed on your machine</p>
            <p>
              2. Install required dependencies:{" "}
              <code className="bg-muted px-2 py-1 rounded text-xs">pip install pandas numpy</code>
            </p>
            <p>3. Download the cleaning script from the Script Generator page</p>
            <p>4. Place your input CSV file in the same directory as the script</p>
            <p>
              5. Run the script: <code className="bg-muted px-2 py-1 rounded text-xs">python clean_data.py</code>
            </p>
            <p>6. Find the cleaned output in cleaned_output.csv</p>
          </div>
        </Card>

        {/* FAQ */}
        <div className="space-y-4">
          <h2 className="text-2xl font-bold">Frequently Asked Questions</h2>
          <Accordion type="single" collapsible className="space-y-2">
            {faqItems.map((item, idx) => (
              <AccordionItem key={idx} value={`item-${idx}`} className="border rounded-lg px-4">
                <AccordionTrigger className="font-semibold py-4">{item.question}</AccordionTrigger>
                <AccordionContent className="text-muted-foreground pb-4">{item.answer}</AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>
    </div>
  )
}
