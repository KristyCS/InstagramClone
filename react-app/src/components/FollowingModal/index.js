import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import Following from './Following';

function FollowingModal({followingCount}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <p onClick={() => setShowModal(true)}>{followingCount} following</p>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <Following />
        </Modal>
      )}
    </>
  );
}

export default FollowingModal;
