# Data-in-QR: Printable QR Labels That Carry Their Own Data

**Turn a spreadsheet into printable QR labels that carry their own
data.** Scan a label to view and copy its contents in a
browser---without maintaining a backend database or relying on a
dedicated app.

[![Watch the video](https://img.youtube.com/vi/nw5yWiItUSc/0.jpg)](https://www.youtube.com/watch?v=nw5yWiItUSc)

## What is it?

Imagine labeling a storage box, workshop tool, laboratory sample, or
piece of equipment. Scan its QR code with a smartphone and a table
appears with the information associated with that object: its name, ID,
specifications, owner, notes, or other fields you chose to include.

The key difference from many conventional QR labels is that **the record
is embedded in the QR code itself**. The reader does not need to look up
the record in a database.

The project uses a CSV file to create printable QR labels and a static
HTML page to display the data. You can copy individual fields or copy
the whole record in a format suitable for a spreadsheet, report, or
other application.

## What can you use it for?

-   **Workshop and hobby storage:** Label boxes, component drawers,
    tools, and 3D-printing supplies.
-   **Equipment identification:** Make model numbers, specifications,
    and replacement-part information available beside equipment.
-   **Laboratory samples:** Associate samples with structured metadata
    and notes.
-   **Warehouse storage:** Print labels showing the contents of bins,
    cartons, or containers.
-   **Product documentation:** Attach product details and reference
    information to physical objects.
-   **Household organization:** Label moving boxes, storage containers,
    and household supplies.
-   **Business Card:** Your customer can scan the QR and copy/paste your contact information without having it exposed to the open web.
     
These are examples, not a claim that the project replaces a full
inventory-management system. It is best suited to relatively small
records that do not change frequently.

## How it works

`CSV file → QR labels containing the data → Browser displays the record`

1.  **Prepare a CSV file.** Include an `id` column and other custom columns for the fields you
    want each record to contain. 
2.  **Generate the labels.** Open the generator in a browser, load the
    CSV, pick a label template, then generate the
    output.
3.  **Print and attach.** Print the labels and attach them to the
    relevant objects. 
4.  **Scan and use the data.** Scan a QR code to open the reader and
    view the record. Copy individual fields or export the record as a
    table.

Each row is encoded as JSON and represented in a Base64URL-encoded URL
fragment (`#data=`). The reader decodes the payload in the browser and
displays the record.

## Quick start

### What you'll need

-   The project HTML files and their required JavaScript libraries.
-   A CSV file containing the records to encode.
-   A modern web browser.
-   A printer if you want physical labels.

### 1. Prepare your CSV

For example:

``` csv
id,item,location,notes
BOX-001,Electronic components,Workshop shelf A,Resistors and capacitors
BOX-002,3D printing supplies,Workshop shelf B,Nozzles and maintenance kit
BOX-003,Test instruments,Workbench,Multimeter accessories
```

The `id` column identifies each record. The other columns become fields
shown by the reader. The `id` information will print as text under the QR, so keep it small!.

### 2. Generate labels

Open `csv_to_qr_generator.html` in your browser and load your CSV file.
Choose the appropriate label layout and configure the base URL so that
the generated QR codes point to your reader page.

Generate the labels and export them in one of the formats supported by
the generator, such as a printable PDF sheet or PNG images.

You can reuse partially printed sheets by starting printing at a specified row, column position in the grid. (Huge paper saver!)

### 3. Print and scan

Print the labels, attach one to an object, and scan it with your phone.
The reader page displays the data embedded in that QR code.

### 4. Copy the information

Use the reader's copy controls to copy individual fields or the full
record. The reader supports exporting data in formats including TSV,
CSV, JSON, and Markdown.

> **Reader URL:** The base URL in each QR code must point to a location
> where `index.html` is accessible. If you host the reader online, a
> phone generally needs an internet connection to load the page. Offline
> use is possible when the reader page and its dependencies are
> available locally (i.e by being cached by the browser).
> Hint: Modify the html source to have your own hosted URL as default.
 
## Why use this instead of a database-backed QR system?

-   **No backend database required:** The record travels inside the QR
    code instead of being fetched from a server-side record store.
-   **Works with ordinary tools:** Use a spreadsheet to prepare the data
    and a browser to generate or read labels.
-   **Portable records:** Anyone who can access the reader can view and
    copy the embedded data without needing an account in a dedicated
    application.
-   **Useful for stable information:** The printed label can continue to
    carry its record without depending on a hosted database remaining
    available.
-   **Multiple fields per code:** Store a small structured record rather
    than only a single identifier or URL.

QR codes can also store data directly, and not every conventional QR
solution requires a database. This project's particular combination is
CSV-based generation, printable labels, an embedded structured record,
and a reusable browser-based reader.

## Limitations and design considerations

-   **The data is static.** If a record changes, you will normally need
    to generate and print a replacement QR code.
-   **QR codes have limited capacity.** Larger records create denser
    codes that may be harder to scan, particularly on small labels.
-   **There is no built-in global search.** Scanning a label displays
    the record in that code; it does not automatically search across all
    generated records.
-   **The payload is not confidential.** Base64URL is an encoding
    format, not encryption. Anyone who obtains the QR code may be able
    to decode its contents. Do not embed passwords, secrets, or
    sensitive information.
-   **Offline use depends on reader availability.** A hosted reader must
    be loaded from its URL. To scan without internet access, the reader
    page and required files must be cached or already be available locally in a
    suitable setup.
-   **No synchronization is provided.** The system does not
    automatically synchronize changes between a CSV file, printed
    labels, or other applications.

For these reasons, the project is most appropriate for small, relatively
stable, non-sensitive records---not live inventory counts, access
control, or workflows that require audit trails and centralized updates.

## Project files

| File | Purpose |
| :--- | :--- |
| `csv_to_qr_generator.html` | Generator interface for importing CSV data, previewing QR codes, and creating label output. |
| `index.html` | Reader page that decodes the embedded payload and displays the record. |
| `qrcode.js` | JavaScript library used to render QR codes locally in the browser. |
| `pdf-lib.js` | JavaScript library used to create PDF label sheets in the browser. |

The JavaScript libraries need to be available in the locations expected
by the HTML files.

## External JavaScript libraries

This project uses the following open-source client-side libraries:

-   [qrcodejs](https://github.com/davidshimjs/qrcodejs) --- QR code
    generation in the browser.
-   [pdf-lib](https://github.com/hopding/pdf-lib) --- Creation and
    modification of PDF documents in JavaScript.

## Contributing

Suggestions and contributions are welcome. Helpful areas include:

-   Additional printable label templates.
-   Example CSV files for different use cases.
-   Improvements to the reader interface and documentation.
-   Testing with different browsers, phones, and printers.
-   Ideas that make the tool easier to use.

Please check the repository's issue tracker, if enabled, before opening
a new issue so that related suggestions can be discussed together.

## License

See the repository's license file for the terms under which this project
may be used, modified, and distributed.

## Disclaimer

Avery is a trademark of Avery Products Corporation. This software is not
affiliated with, sponsored by, or endorsed by Avery Products
Corporation.
