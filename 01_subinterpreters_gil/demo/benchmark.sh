echo "=== Starting tests with GIL enabled ==="

# uv python pin cpython-3.14.5-macos-aarch64-none
# uv sync

echo "=== BASELINE ==="
for i in {1..5}; do uv run 00_baseline.py; done

echo "=== MULTIPROCESS ==="
for i in {1..5}; do uv run 01_multiprocess.py 1; done
for i in {1..5}; do uv run 01_multiprocess.py 2; done
for i in {1..5}; do uv run 01_multiprocess.py 4; done
for i in {1..5}; do uv run 01_multiprocess.py 8; done

echo "=== MULTITHREAD ==="
for i in {1..5}; do uv run 02_multithread.py 1; done
for i in {1..5}; do uv run 02_multithread.py 2; done
for i in {1..5}; do uv run 02_multithread.py 4; done
for i in {1..5}; do uv run 02_multithread.py 8; done

echo "=== MULTIINTERPRETER ==="
for i in {1..5}; do uv run 07_multiinterpreter.py 1; done
for i in {1..5}; do uv run 07_multiinterpreter.py 2; done
for i in {1..5}; do uv run 07_multiinterpreter.py 4; done
for i in {1..5}; do uv run 07_multiinterpreter.py 8; done


# echo "=== Starting tests with GIL disabled ==="
# uv python pin cpython-3.14.5+freethreaded-macos-aarch64-none
# uv sync

# echo "=== MULTIPROCESS ==="
# for i in {1..5}; do uv run 01_multiprocess.py 1; done
# for i in {1..5}; do uv run 01_multiprocess.py 2; done
# for i in {1..5}; do uv run 01_multiprocess.py 4; done
# for i in {1..5}; do uv run 01_multiprocess.py 8; done

# echo "=== MULTITHREAD ==="
# for i in {1..5}; do uv run 02_multithread.py 1; done
# for i in {1..5}; do uv run 02_multithread.py 2; done
# for i in {1..5}; do uv run 02_multithread.py 4; done
# for i in {1..5}; do uv run 02_multithread.py 8; done

# echo "=== MULTIINTERPRETER ==="
# for i in {1..5}; do uv run 06_multiinterpreter.py 1; done
# for i in {1..5}; do uv run 06_multiinterpreter.py 2; done
# for i in {1..5}; do uv run 06_multiinterpreter.py 4; done
# for i in {1..5}; do uv run 06_multiinterpreter.py 8; done
