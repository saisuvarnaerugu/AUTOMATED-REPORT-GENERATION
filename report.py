import pandas as pd
from fpdf import FPDF

# Step 1: Load and analyze the data
data = pd.read_csv('data.csv')

# Basic analysis
average_score = data['Score'].mean()
max_score = data['Score'].max()
min_score = data['Score'].min()
top_scorer = data.loc[data['Score'].idxmax(), 'Name']

# Step 2: Create PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Student Scores Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_summary(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Average Score: {average_score:.2f}', ln=True)
        self.cell(0, 10, f'Highest Score: {max_score} ({top_scorer})', ln=True)
        self.cell(0, 10, f'Lowest Score: {min_score}', ln=True)
        self.ln(10)

    def add_table(self, dataframe):
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Name', 1)
        self.cell(40, 10, 'Score', 1)
        self.ln()

        self.set_font('Arial', '', 12)
        for index, row in dataframe.iterrows():
            self.cell(60, 10, row['Name'], 1)
            self.cell(40, 10, str(row['Score']), 1)
            self.ln()

# Step 3: Generate PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_summary()
pdf.add_table(data)
pdf.output('report.pdf')

print("PDF report generated as 'report.pdf'")
