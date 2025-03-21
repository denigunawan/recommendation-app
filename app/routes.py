from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Asset

api_bp = Blueprint("api", __name__)

# 📌 1️⃣ Get All Assets (READ)
@api_bp.route("/assets", methods=["GET"])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.to_dict() for asset in assets])

# 📌 2️⃣ Get Asset by ID (READ)
@api_bp.route("/assets/<int:asset_id>", methods=["GET"])
def get_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({"error": "Asset not found"}), 404
    return jsonify(asset.to_dict())

# 📌 3️⃣ Create New Asset (CREATE)
@api_bp.route("/assets", methods=["POST"])
def create_asset():
    data = request.json
    new_asset = Asset(
        no_assets=data.get("no_assets"),
        tanggal_diterima=data.get("tanggal_diterima"),
        nama=data.get("nama"),
        quantity=data.get("quantity"),
        harga_assets=data.get("harga_assets"),
        tanggal_input=data.get("tanggal_input"),
        vendor=data.get("vendor"),
        jenis=data.get("jenis"),
        user_id=data.get("user_id"),
    )
    db.session.add(new_asset)
    db.session.commit()
    return jsonify(new_asset.to_dict()), 201

# 📌 4️⃣ Update Asset (UPDATE)
@api_bp.route("/assets/<int:asset_id>", methods=["PUT"])
def update_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({"error": "Asset not found"}), 404

    data = request.json
    asset.no_assets = data.get("no_assets", asset.no_assets)
    asset.tanggal_diterima = data.get("tanggal_diterima", asset.tanggal_diterima)
    asset.nama = data.get("nama", asset.nama)
    asset.quantity = data.get("quantity", asset.quantity)
    asset.harga_assets = data.get("harga_assets", asset.harga_assets)
    asset.tanggal_input = data.get("tanggal_input", asset.tanggal_input)
    asset.vendor = data.get("vendor", asset.vendor)
    asset.jenis = data.get("jenis", asset.jenis)
    asset.user_id = data.get("user_id", asset.user_id)

    db.session.commit()
    return jsonify(asset.to_dict())

# 📌 5️⃣ Delete Asset (DELETE)
@api_bp.route("/assets/<int:asset_id>", methods=["DELETE"])
def delete_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({"error": "Asset not found"}), 404

    db.session.delete(asset)
    db.session.commit()
    return jsonify({"message": "Asset deleted successfully"}), 200